# DisplayWhenAdded Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded`

Gets or sets whether new sketch entities are immediately displayed when created.
Gets or sets whether new sketch entities are immediately displayed when created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayWhenAdded As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
instance.DisplayWhenAdded = value
 
value = instance.DisplayWhenAdded
```

```

System.bool DisplayWhenAdded {get; set;}
```

```

property System.bool DisplayWhenAdded {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display new sketch entities when added, false to not

Remarks

The sketch entities appear on the screen after performing [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) or [IModelView::IGraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md) or [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) is performed. Also, [ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) must be true to use this method's settings.

This display setting remains even after your program run has ended. Therefore, it is recommended that you reset this parameter to TRUE at the end of your program. For example, if you have ended your program and the display is set to FALSE, then the user would have difficulty performing selections and newly created entities would not be seen until a redraw or a rebuild.

NOTES:

- IModelView::GraphicsRedraw and IModelView::IGraphicsRedraw are much faster than IModelDoc2::EditRebuild3.
- ISketchManager::AddToDB and ISketchManager::DisplayWhenAdded also increase performance during sketch entity creation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
