# UpdateAllGraphicsLayers Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~UpdateAllGraphicsLayers`

Gets or sets whether to update all graphic layers in any mode.
Gets or sets whether to update all graphic layers in any mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpdateAllGraphicsLayers As System.Boolean
```

```

Dim instance As IModelView
Dim value As System.Boolean
 
instance.UpdateAllGraphicsLayers = value
 
value = instance.UpdateAllGraphicsLayers
```

```

System.bool UpdateAllGraphicsLayers {get; set;}
```

```

property System.bool UpdateAllGraphicsLayers {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable all graphic layers in any mode, false to not

Remarks

SceneGraph organizes contents into layer 0 and 1. Layer 0 contains general geometry, and layer 1 contains sketch geometry. By default this property is set to false, which means only layer 1 is updated when in edit mode. When this property is set to true, then all layers are updated regardless of mode, including edit mode.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
