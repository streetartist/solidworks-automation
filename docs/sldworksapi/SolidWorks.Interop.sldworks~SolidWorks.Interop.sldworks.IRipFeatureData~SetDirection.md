# SetDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~SetDirection`

Sets the direction for this rip feature.
Sets the direction for this rip feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDirection( _
   ByVal Edge As System.Object, _
   ByVal Dir As System.Integer _
) 
```

```

Dim instance As IRipFeatureData
Dim Edge As System.Object
Dim Dir As System.Integer
 
instance.SetDirection(Edge, Dir)
```

```

void SetDirection( 
   System.object Edge,
   System.int Dir
)
```

```

void SetDirection( 
   System.Object^ Edge,
   System.int Dir
) 
```

#### Parameters

*Edge*
:   Rip feature [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*Dir*
:   Direction of rip feature:

    - 0 = this direction
    - 1 = other direction
    - 2 = both directions

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md)  
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.md)  
[IRipFeatureData::GetDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetDirection.md)
