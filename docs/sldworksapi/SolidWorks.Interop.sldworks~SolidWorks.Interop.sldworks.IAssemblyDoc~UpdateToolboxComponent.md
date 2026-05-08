# UpdateToolboxComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateToolboxComponent`

Updates SOLIDWORKS Toolbox components in the specified assembly level using the current information in Toolbox settings.
Updates SOLIDWORKS Toolbox components in the specified assembly level using the current information in Toolbox settings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateToolboxComponent( _
   ByVal AssemblyLevelToUpdate As System.Integer _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim AssemblyLevelToUpdate As System.Integer
Dim value As System.Integer
 
value = instance.UpdateToolboxComponent(AssemblyLevelToUpdate)
```

```

System.int UpdateToolboxComponent( 
   System.int AssemblyLevelToUpdate
)
```

```

System.int UpdateToolboxComponent( 
   System.int AssemblyLevelToUpdate
) 
```

#### Parameters

*AssemblyLevelToUpdate*
:   Level in which to update SOLIDWORKS Toolbox components as defined in [swAssemblyLevelToUpdate\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyLevelToUpdate_e.html)

#### Return Value

Status of updating the SOLIDWORKS Toolbox components as defined in [swAssemblyUpdateToolboxComponentStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyUpdateToolboxComponentStatus_e.html)

Example

[Update All Toolbox Components (C#)](Update_All_Toolbox_Components_Example_CSharp.htm)  
[Update All Toolbox Components (VB.NET)](Update_All_Toolbox_Components_Example_VBNET.htm)  
[Update All Toolbox Components (VBA)](Update_All_Toolbox_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
