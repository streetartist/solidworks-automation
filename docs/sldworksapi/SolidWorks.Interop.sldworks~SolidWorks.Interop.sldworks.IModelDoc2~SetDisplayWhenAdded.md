# SetDisplayWhenAdded Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded`

Obsolete. Superseded by ISketchManager::DisplayWhenAdded.
Obsolete. Superseded by [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDisplayWhenAdded( _
   ByVal Setting As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Setting As System.Boolean
 
instance.SetDisplayWhenAdded(Setting)
```

```

void SetDisplayWhenAdded( 
   System.bool Setting
)
```

```

void SetDisplayWhenAdded( 
   System.bool Setting
) 
```

#### Parameters

*Setting*
:   True to display new sketch entities when added, false to note

Remarks

The sketch entities appear on the screen after performing [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) or [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) is performed. Also, [IModelDoc2::SetAddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.md) must be True to use this method's settings.

This display setting remains even after your program run has ended. Therefore, it is recommended that you reset this parameter to True at the end of your program. For example, if you have ended your program and the display is set to false, then the user would have difficulty performing selections and newly created entities would not be seen until a redraw or a rebuild.

NOTES:

- IModelDoc2::GraphicsRedraw2 is much faster than ModelDoc2::EditRebuild3.
- IModelDoc2::SetAddToDB and [IModelDoc2::SetDisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.md) also increase performance during sketch entity creation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetDisplayWhenAdded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDisplayWhenAdded.md)
