# AutoSpaceComponentsOnDrag Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~AutoSpaceComponentsOnDrag`

Gets or sets whether to automatically space a group of components equally along an axis as you drag them.
Gets or sets whether to automatically space a group of components equally along an axis as you drag them.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSpaceComponentsOnDrag As System.Boolean
```

```

Dim instance As IExplodeStep
Dim value As System.Boolean
 
instance.AutoSpaceComponentsOnDrag = value
 
value = instance.AutoSpaceComponentsOnDrag
```

```

System.bool AutoSpaceComponentsOnDrag {get; set;}
```

```

property System.bool AutoSpaceComponentsOnDrag {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically space components equally along an axis as you drag them, false to not (see **Remarks**)

Remarks

If this property is set to true, then, by default, [IExplodeStep::RotateAboutEachComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotateAboutEachComponentOrigin.md) is false and [IExplodeStep::RotationAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotationAngle.md) is 0.0.

If you set this property to false during editing of this step, then you must re-set the values for IExplodeStep::RotateAboutEachComponentOrigin and IExplodeStep::RotationAngle.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
