# FeatureCircularPattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern`

Obsolete. Superseded by IFeatureManager::FeatureCircularPattern2.
Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureCircularPattern( _
   ByVal Num As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal DName As System.String _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Num As System.Integer
Dim Spacing As System.Double
Dim FlipDir As System.Boolean
Dim DName As System.String
Dim value As Feature
 
value = instance.FeatureCircularPattern(Num, Spacing, FlipDir, DName)
```

```

Feature FeatureCircularPattern( 
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.string DName
)
```

```

Feature^ FeatureCircularPattern( 
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.String^ DName
) 
```

#### Parameters

*Num*

*Spacing*

*FlipDir*

*DName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
