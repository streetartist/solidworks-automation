# OriginOnCurve Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~OriginOnCurve`

Gets or sets whether to place the origin on the curve for this reference plane feature.
Gets or sets whether to place the origin on the curve for this reference plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OriginOnCurve As System.Boolean
```

```

Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean
 
instance.OriginOnCurve = value
 
value = instance.OriginOnCurve
```

```

System.bool OriginOnCurve {get; set;}
```

```

property System.bool OriginOnCurve {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to place the origin on the curve, false to place the origin on the vertex or point

Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)
