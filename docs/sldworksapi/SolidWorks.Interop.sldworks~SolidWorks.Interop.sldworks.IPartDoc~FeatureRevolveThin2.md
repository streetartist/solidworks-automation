# FeatureRevolveThin2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureRevolveThin2`

Obsolete. Superseded by IFeatureManager::FeatureRevolveThin.
Obsolete. Superseded by [IFeatureManager::FeatureRevolveThin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureRevolveThin2( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ReverseThinDir As System.Integer, _
   ByVal Merge As System.Boolean _
) 
```

```

Dim instance As IPartDoc
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ReverseThinDir As System.Integer
Dim Merge As System.Boolean
 
instance.FeatureRevolveThin2(Angle, ReverseDir, Angle2, RevType, Thickness1, Thickness2, ReverseThinDir, Merge)
```

```

void FeatureRevolveThin2( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool Merge
)
```

```

void FeatureRevolveThin2( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool Merge
) 
```

#### Parameters

*Angle*

*ReverseDir*

*Angle2*

*RevType*

*Thickness1*

*Thickness2*

*ReverseThinDir*

*Merge*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
