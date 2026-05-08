# GraphicsRedrawEnabled Property (ICollisionDetectionManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GraphicsRedrawEnabled`

Gets or sets whether to display components in their transformed positions.
Gets or sets whether to display components in their transformed positions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GraphicsRedrawEnabled As System.Boolean
```

```

Dim instance As ICollisionDetectionManager
Dim value As System.Boolean
 
instance.GraphicsRedrawEnabled = value
 
value = instance.GraphicsRedrawEnabled
```

```

System.bool GraphicsRedrawEnabled {get; set;}
```

```

property System.bool GraphicsRedrawEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display components in their transformed positions, false to display components in their last known positions

Remarks

If this property is set to false, the graphics display update is drastically reduced. The client application may force the assembly to be redrawn by calling [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Set this property to false for maximum performance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md)  
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.md)
