# CustomPropertyManager Property (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager`

Gets the custom properties for this document or configuration.
Gets the custom properties for this document or configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CustomPropertyManager( _
   ByVal ConfigName As System.String _
) As CustomPropertyManager
```

```

Dim instance As IModelDocExtension
Dim ConfigName As System.String
Dim value As CustomPropertyManager
 
value = instance.CustomPropertyManager(ConfigName)
```

```

CustomPropertyManager CustomPropertyManager( 
   System.string ConfigName
) {get;}
```

```

property CustomPropertyManager^ CustomPropertyManager {
   CustomPropertyManager^ get(System.String^ ConfigName);
}
```

#### Parameters

*ConfigName*
:   Name of configuration

#### Property Value

[ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md) object

Remarks

File custom information is stored in the document file. It can be:

- General to the file, in which case there is a single value whatever the model's configuration

   - or -

- Configuration-specific, in which case a different value may be set for each configuration in the model

To access a general custom information value, set the configuration argument to an empty string. To get a document-level property, pass an empty string ("") to the configuration argument.

As per Microsoft recommendations for OLE support, the file summary information for SOLIDWORKS documents is written as an OLE property set into a stream named "\005Summary Information" off the root storage of the SOLIDWORKS document's compound file.

NOTE: MFC does not currently provide classes that manage summary information. However, the DRAWCLI application shipped with Visual C++ includes a sample implementation, in the form of the class CSummInfo, that you can use as an example when implementing your own. This class is used by the document class CDrawDoc. DRAWCLI also includes property pages for displaying and modifying Summary Information.

Example

[Get Custom Properties of Referenced Part (C#)](Get_Custom_Properties_of_Referenced_Part_Example_CSharp.htm)  
[Get Custom Properties of Referenced Part (VB.NET)](Get_Custom_Properties_of_Referenced_Part_Example_VBNET.htm)  
[Get Custom Properties of Referenced Part (VBA)](Get_Custom_Properties_of_Referenced_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IConfiguration::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md)  
[IFeature::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CustomPropertyManager.md)
