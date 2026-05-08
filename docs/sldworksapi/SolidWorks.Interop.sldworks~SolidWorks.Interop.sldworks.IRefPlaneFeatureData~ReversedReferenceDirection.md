# ReversedReferenceDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReversedReferenceDirection`

Gets or sets whether to reverse the direction of the specified reference for this reference plane feature.
Gets or sets whether to reverse the direction of the specified reference for this reference plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReversedReferenceDirection( _
   ByVal ReferenceIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As IRefPlaneFeatureData
Dim ReferenceIndex As System.Integer
Dim value As System.Boolean
 
instance.ReversedReferenceDirection(ReferenceIndex) = value
 
value = instance.ReversedReferenceDirection(ReferenceIndex)
```

```

System.bool ReversedReferenceDirection( 
   System.int ReferenceIndex
) {get; set;}
```

```

property System.bool ReversedReferenceDirection {
   System.bool get(System.int ReferenceIndex);
   void set (System.int ReferenceIndex, System.bool value);
}
```

#### Parameters

*ReferenceIndex*
:   Index of the reference whose direction to set as defined in [swRefPlaneReferenceIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceIndex_e.html)

#### Property Value

True to reverse the direction of the specified reference, false to not

Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)  
[IRefPlaneFeatureData::Reference Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.md)
