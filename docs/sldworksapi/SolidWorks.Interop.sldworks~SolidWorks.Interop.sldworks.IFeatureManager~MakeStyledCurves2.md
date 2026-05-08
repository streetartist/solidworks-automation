# MakeStyledCurves2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MakeStyledCurves2`

Fits a spline to the preselected sketch segments to make a smooth edge on the model.
Fits a spline to the preselected sketch segments to make a smooth edge on the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeStyledCurves2( _
   ByVal Tolerance As System.Double, _
   ByVal Mode As System.Integer _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Tolerance As System.Double
Dim Mode As System.Integer
Dim value As System.Boolean
 
value = instance.MakeStyledCurves2(Tolerance, Mode)
```

```

System.bool MakeStyledCurves2( 
   System.double Tolerance,
   System.int Mode
)
```

```

System.bool MakeStyledCurves2( 
   System.double Tolerance,
   System.int Mode
) 
```

#### Parameters

*Tolerance*
:   Deviation permitted from the selected geometry

*Mode*
:   - 1 = Convert the selected geometry to construction geometry
    - 11 = delete the selected geometry

#### Return Value

True if fit spline is created, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
