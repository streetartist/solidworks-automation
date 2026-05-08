# SetIsFlipped Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetIsFlipped`

Gets whether the chamfer feature is flipped.
Gets whether the chamfer feature is flipped.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetIsFlipped( _
   ByVal Entity As System.Object, _
   ByVal Flip As System.Boolean _
) 
```

```

Dim instance As IChamferFeatureData2
Dim Entity As System.Object
Dim Flip As System.Boolean
 
instance.SetIsFlipped(Entity, Flip)
```

```

void SetIsFlipped( 
   System.object Entity,
   System.bool Flip
)
```

```

void SetIsFlipped( 
   System.Object^ Entity,
   System.bool Flip
) 
```

#### Parameters

*Entity*
:   Chamfer feature

*Flip*
:   True flips the chamfer feature, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::GetIsFlipped Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetIsFlipped.md)
