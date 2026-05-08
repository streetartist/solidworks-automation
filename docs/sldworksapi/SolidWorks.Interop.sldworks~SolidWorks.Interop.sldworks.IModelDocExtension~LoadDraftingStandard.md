# LoadDraftingStandard Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LoadDraftingStandard`

Loads a custom drafting standard from a file.
Loads a custom drafting standard from a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadDraftingStandard( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.LoadDraftingStandard(FileName)
```

```

System.bool LoadDraftingStandard( 
   System.string FileName
)
```

```

System.bool LoadDraftingStandard( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and filename of the drafting standard to load

#### Return Value

True if the specified drafting standard is loaded, false if not

Example

[Change Drafting Standard to Custom (VBA)](Change_Drafting_Standard_to_Custom_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CopyDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CopyDraftingStandard.md)  
[IModelDocExtension::DeleteDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDraftingStandard.md)  
[IModelDocExtension::GetDraftingStandardNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDraftingStandardNames.md)  
[IModelDocExtension::RenameDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDraftingStandard.md)  
[IModelDocExtension::SaveDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDraftingStandard.md)
