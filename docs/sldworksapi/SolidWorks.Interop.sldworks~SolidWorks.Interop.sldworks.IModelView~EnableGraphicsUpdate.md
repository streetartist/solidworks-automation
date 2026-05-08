# EnableGraphicsUpdate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~EnableGraphicsUpdate`

Gets or sets whether or not to refresh the model view.
Gets or sets whether or not to refresh the model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableGraphicsUpdate As System.Boolean
```

```

Dim instance As IModelView
Dim value As System.Boolean
 
instance.EnableGraphicsUpdate = value
 
value = instance.EnableGraphicsUpdate
```

```

System.bool EnableGraphicsUpdate {get; set;}
```

```

property System.bool EnableGraphicsUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to refresh the model view, false to not

Remarks

This property affects whether to refresh the model view during a selection, such as [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md) or [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
