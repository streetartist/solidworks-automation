# AngleOrDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~AngleOrDistance`

Gets or sets the angle or distance of the specified reference for this reference plane feature.
Gets or sets the angle or distance of the specified [reference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.md) for this reference plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AngleOrDistance( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IRefPlaneFeatureData
Dim Index As System.Integer
Dim value As System.Double
 
instance.AngleOrDistance(Index) = value
 
value = instance.AngleOrDistance(Index)
```

```

System.double AngleOrDistance( 
   System.int Index
) {get; set;}
```

```

property System.double AngleOrDistance {
   System.double get(System.int Index);
   void set (System.int Index, System.double value);
}
```

#### Parameters

*Index*
:   Index of the specified reference as defined in [swRefPlaneReferenceIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceIndex_e.html)

#### Property Value

Angle or distance

Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)  
[IRefPlaneFeatureData::Reference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.md)
