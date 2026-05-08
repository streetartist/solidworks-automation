# MakeStackedBalloon Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon`

Converts this balloon to a stacked balloon.
Converts this balloon to a stacked balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub MakeStackedBalloon( _
   ByVal StackedBalloonOptions As System.Object _
) 
```

```

Dim instance As INote
Dim StackedBalloonOptions As System.Object
 
instance.MakeStackedBalloon(StackedBalloonOptions)
```

```

void MakeStackedBalloon( 
   System.object StackedBalloonOptions
)
```

```

void MakeStackedBalloon( 
   System.Object^ StackedBalloonOptions
) 
```

#### Parameters

*StackedBalloonOptions*
:   [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)

Remarks

Before calling this method, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the entity to add to the balloon stack.

After calling this method to convert the balloon to a stacked balloon, add more balloons by calling:

1. [INote::GetBalloonStack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.md)
2. [IBalloonStack::AddTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~AddTo.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[IModelDocExtension::InsertStackedBalloon2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.md)  
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.md)
