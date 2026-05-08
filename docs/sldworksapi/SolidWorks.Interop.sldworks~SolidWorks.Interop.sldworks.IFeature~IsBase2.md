# IsBase2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsBase2`

Gets whether this feature is a base feature.
Gets whether this feature is a base feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsBase2() As System.Boolean
```

```

Dim instance As IFeature
Dim value As System.Boolean
 
value = instance.IsBase2()
```

```

System.bool IsBase2()
```

```

System.bool IsBase2(); 
```

#### Return Value

True if this is a base feature, false if not

Remarks

Any feature that creates a solid body is a base feature. For example:

- An extrude operation creates a solid body; therefore, that feature is a base feature.
- A body imported via an IGES file is a base feature.

However, a fillet operation does not create a solid body; therefore, that feature is not a base feature.

In a multibody environment, more than one feature can return true. Thus, a lot of features can be base features in a multibody environment.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::ISetBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.md)  
[IFeature::SetBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody2.md)
