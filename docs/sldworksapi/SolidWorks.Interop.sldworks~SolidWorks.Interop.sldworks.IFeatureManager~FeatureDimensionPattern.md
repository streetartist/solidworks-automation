# FeatureDimensionPattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureDimensionPattern`

Not implemented.
Not implemented.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureDimensionPattern( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal DiagonalOnly As System.Boolean, _
   ByVal DName1 As System.String, _
   ByVal DName2 As System.String, _
   ByVal VaryInstance As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Num1 As System.Integer
Dim Spacing1 As System.Double
Dim Num2 As System.Integer
Dim Spacing2 As System.Double
Dim DiagonalOnly As System.Boolean
Dim DName1 As System.String
Dim DName2 As System.String
Dim VaryInstance As System.Boolean
Dim value As Feature
 
value = instance.FeatureDimensionPattern(Num1, Spacing1, Num2, Spacing2, DiagonalOnly, DName1, DName2, VaryInstance)
```

```

Feature FeatureDimensionPattern( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool DiagonalOnly,
   System.string DName1,
   System.string DName2,
   System.bool VaryInstance
)
```

```

Feature^ FeatureDimensionPattern( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool DiagonalOnly,
   System.String^ DName1,
   System.String^ DName2,
   System.bool VaryInstance
) 
```

#### Parameters

*Num1*

*Spacing1*

*Num2*

*Spacing2*

*DiagonalOnly*

*DName1*

*DName2*

*VaryInstance*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
