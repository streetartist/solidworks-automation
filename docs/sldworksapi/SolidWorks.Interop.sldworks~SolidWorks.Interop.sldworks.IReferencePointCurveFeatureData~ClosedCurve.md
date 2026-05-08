# ClosedCurve Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ClosedCurve`

Gets or sets whether the curve is closed or not.
Gets or sets whether the curve is closed or not.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ClosedCurve As System.Boolean
```

```

Dim instance As IReferencePointCurveFeatureData
Dim value As System.Boolean
 
instance.ClosedCurve = value
 
value = instance.ClosedCurve
```

```

System.bool ClosedCurve {get; set;}
```

```

property System.bool ClosedCurve {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if curve is closed, false if not

Example

See the [IReferencePointCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.md)  
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.md)
