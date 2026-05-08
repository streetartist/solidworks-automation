# GetBaseCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBaseCurve`

Gets the base curve for this trimmed curve.
Gets the base curve for this trimmed curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBaseCurve() As Curve
```

```

Dim instance As ICurve
Dim value As Curve
 
value = instance.GetBaseCurve()
```

```

Curve GetBaseCurve()
```

```

Curve^ GetBaseCurve(); 
```

#### Return Value

Pointer to the [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) object

Remarks

This method is a geometry function that applies only to SOLIDWORKS API applications.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)
