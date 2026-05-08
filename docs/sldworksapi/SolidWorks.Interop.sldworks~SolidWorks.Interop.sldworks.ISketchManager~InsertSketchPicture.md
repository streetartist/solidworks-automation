# InsertSketchPicture Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture`

Obsolete. Superseded by ISketchManager::InsertSketchPicture2.
Obsolete. Superseded by [ISketchManager::InsertSketchPicture2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSketchPicture( _
   ByVal FileName As System.String _
) As SketchPicture
```

```

Dim instance As ISketchManager
Dim FileName As System.String
Dim value As SketchPicture
 
value = instance.InsertSketchPicture(FileName)
```

```

SketchPicture InsertSketchPicture( 
   System.string FileName
)
```

```

SketchPicture^ InsertSketchPicture( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path to image file including file extension

#### Return Value

[Picture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
