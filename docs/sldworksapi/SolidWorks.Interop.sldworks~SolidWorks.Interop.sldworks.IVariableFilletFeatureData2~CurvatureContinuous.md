# CurvatureContinuous Property (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~CurvatureContinuous`

Gets or sets whether to create a smoother curvature between adjacent surfaces for this variable radius fillet feature.
Gets or sets whether to create a smoother curvature between adjacent surfaces for this variable radius fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurvatureContinuous As System.Boolean
```

```

Dim instance As IVariableFilletFeatureData2
Dim value As System.Boolean
 
instance.CurvatureContinuous = value
 
value = instance.CurvatureContinuous
```

```

System.bool CurvatureContinuous {get; set;}
```

```

property System.bool CurvatureContinuous {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to make curvatures continuous, false to not

Remarks

This property supersedes any [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.md) setting. Curvature continuous fillets are smoother than standard fillets because there is no jump in curvature at the boundary.

Example

[Create Curvature Continuous Variable Fillet Feature (C#)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_CSharp.htm)  
[Create Curvature Continuous Variable Fillet Feature (VB.NET)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VBNET.htm)  
[Create Curvature Continuous Variable Fillet Feature (VBA)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)
