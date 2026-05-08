# Save Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save`

Saves the block definition.
Saves the block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Save( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ISketchBlockDefinition
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.Save(FileName)
```

```

System.bool Save( 
   System.string FileName
)
```

```

System.bool Save( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path, filename, and filename extension of .sldblk to which to save the block definition

#### Return Value

True if the block definition is saved, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~FileName.md)  
[ISketchBlockDefinition::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile.md)  
[ISketchBlockDefinition::MakeSketchBlockFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md)  
[ISketchBlockDefinition::MakeSketchBlockFromSelected Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md)  
[ISketchBlockDefinition::MakeSketchBlockFromSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md)
