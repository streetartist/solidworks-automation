# GetReferencePointsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount`

Gets the number of reference points for this dimension.
Gets the number of reference points for this dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferencePointsCount() As System.Integer
```

```

Dim instance As IDimension
Dim value As System.Integer
 
value = instance.GetReferencePointsCount()
```

```

System.int GetReferencePointsCount()
```

```

System.int GetReferencePointsCount(); 
```

#### Return Value

Number of dimension reference points

Remarks

Call this method before calling [IDimension::IGetReferencePoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::ISetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.md)  
[IDimension::ReferencePoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.md)
