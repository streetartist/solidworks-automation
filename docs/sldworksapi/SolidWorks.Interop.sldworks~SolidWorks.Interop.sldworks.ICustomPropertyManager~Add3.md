# Add3 Method (ICustomPropertyManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add3`

Adds a custom property to a configuration or model document.
Adds a custom property to a configuration or model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Add3( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.Integer, _
   ByVal FieldValue As System.String, _
   ByVal OverwriteExisting As System.Integer _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldType As System.Integer
Dim FieldValue As System.String
Dim OverwriteExisting As System.Integer
Dim value As System.Integer
 
value = instance.Add3(FieldName, FieldType, FieldValue, OverwriteExisting)
```

```

System.int Add3( 
   System.string FieldName,
   System.int FieldType,
   System.string FieldValue,
   System.int OverwriteExisting
)
```

```

System.int Add3( 
   System.String^ FieldName,
   System.int FieldType,
   System.String^ FieldValue,
   System.int OverwriteExisting
) 
```

#### Parameters

*FieldName*
:   Name of custom property

*FieldType*
:   Type of custom property as defined in [swCustomInfoType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)

*FieldValue*
:   Value of custom property

*OverwriteExisting*
:   Overwrite option as defined in [swCustomPropertyAddOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomPropertyAddOption_e.html)

#### Return Value

Result code as defined in [swCustomInfoAddResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoAddResult_e.html)

Example

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)  
[Get Custom Properties for Configuration (VB.NET)](Get_Custom_Properties_for_Configuration_Example_VBNET.htm)  
[Get Custom Properties for Configuration (C#)](Get_Custom_Properties_for_Configuration_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::Delete2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete2.md)  
[ICustomPropertyManager::Set2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.md)
