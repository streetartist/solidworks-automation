# ObjectSizesAway Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ObjectSizesAway`

Helps define the perspective of the current model view by relating the size of a displayed object with the distance of the object from the observer.
Helps define the perspective of the current model view by relating the size of a displayed object with the distance of the object from the observer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ObjectSizesAway As System.Double
```

```

Dim instance As IModelView
Dim value As System.Double
 
instance.ObjectSizesAway = value
 
value = instance.ObjectSizesAway
```

```

System.double ObjectSizesAway {get; set;}
```

```

property System.double ObjectSizesAway {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance of the object from the observer, relative to the size of the object

Remarks

This property controls the same value as the view, display, perspective information dialog box. It gives the ratio of the distance of the object from the observer to the size of the object. The smaller the value, the greater the amount of perspective distortion.

You can only modify or get this property when the current model view has the perspective display enabled. See [IModelView::AddPerspective](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.md) and [IModelView::RemovePerspective](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.md). If perspective display is disabled, getting the property returns -1, and setting the property has no effect.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.md)
