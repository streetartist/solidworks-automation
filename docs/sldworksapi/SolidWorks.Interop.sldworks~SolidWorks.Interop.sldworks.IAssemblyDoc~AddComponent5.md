# AddComponent5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5`

Adds the specified component for the specified configuration options to this assembly.
Adds the specified component for the specified configuration options to this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddComponent5( _
   ByVal CompName As System.String, _
   ByVal ConfigOption As System.Integer, _
   ByVal NewConfigName As System.String, _
   ByVal UseConfigForPartReferences As System.Boolean, _
   ByVal ExistingConfigName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim ConfigOption As System.Integer
Dim NewConfigName As System.String
Dim UseConfigForPartReferences As System.Boolean
Dim ExistingConfigName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2
 
value = instance.AddComponent5(CompName, ConfigOption, NewConfigName, UseConfigForPartReferences, ExistingConfigName, X, Y, Z)
```

```

Component2 AddComponent5( 
   System.string CompName,
   System.int ConfigOption,
   System.string NewConfigName,
   System.bool UseConfigForPartReferences,
   System.string ExistingConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

Component2^ AddComponent5( 
   System.String^ CompName,
   System.int ConfigOption,
   System.String^ NewConfigName,
   System.bool UseConfigForPartReferences,
   System.String^ ExistingConfigName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*CompName*
:   Path name of a pre-loaded part or assembly to add as a component (see **Remarks**)

*ConfigOption*
:   Mode in which to open the document as specified in [swAddComponentConfigOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddComponentConfigOptions_e.html)

*NewConfigName*
:   Name for the new assembly configuration;

    valid only if ConfigOption =

    - swAddComponentConfigOptions\_e.swAddComponentConfigOptions\_NewConfigWithAllReferenceModels - or -
    - swAddComponentConfigOptions\_e.swAddComponentConfigOptions\_NewConfigWithAsmStructure

*UseConfigForPartReferences*
:   If true, the configuration specified in ExistingConfigName is used

*ExistingConfigName*
:   Name of the configuration of the loaded component; valid only if UseConfigForPartReferences = true

*X*
:   X coordinate of the component center

*Y*
:   Y coordinate of the component center

*Z*
:   Z coordinate of the component center

#### Return Value

[IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

The specified file must be loaded in memory. A file is loaded into memory when you load the file in your SOLIDWORKS session ([ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)) or open an assembly that already contains the file.

To add a new instance of an existing virtual component, use [IComponent2::GetPathName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPathName.md) to get the virtual component's path and file name.

If you want to add the component at a position relative to the root component, use [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md) to reposition the component immediately after calling this method. Or, you can use [IAssemblyDoc::AddComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.md) or [IAssemblyDoc::AddComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.md) to specify the transform when inserting a component, insert as many components as you want at once, and rotate and scale the component through the transform matrix.

IMPORTANT: X, Y, and Z are relative to the bounding box of the component. Use this method to approximately position the component. Then use IComponent2::Transform2 to more precisely position the component.

Example

[Insert New Instance of Virtual Component (VBA)](Insert_New_Instance_of_Virtual_Component_Example_VB.htm)  
[Insert New Instance of Virtual Component (VB.NET)](Insert_New_Instance_of_Virtual_Component_Example_VBNET.htm)  
[Insert New Instance of Virtual Component (C#)](Insert_New_Instance_of_Virtual_Component_Example_CSharp.htm)  
[Add Component and Mate (VBA)](Add_Component_and_Mate_Example_VB.htm)  
[Add Component and Mate (VB.NET)](Add_Component_and_Mate_Example_VBNET.htm)  
[Add Component and Mate (C#)](Add_Component_and_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::InsertEnvelope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertEnvelope.md)  
[IAssemblyDoc::ReplaceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.md)  
[IAssemblyDoc::CopyWithMates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CopyWithMates.md)  
[IAssemblyDoc::InsertImportedComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent.md)
