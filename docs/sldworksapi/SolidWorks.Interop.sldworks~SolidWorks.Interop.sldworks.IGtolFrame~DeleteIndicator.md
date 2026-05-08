# DeleteIndicator Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~DeleteIndicator`

Deletes the tolerance indicator at the specified Gtol frame indicator index.
Deletes the tolerance indicator at the specified Gtol frame indicator index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteIndicator( _
   ByVal IndicatorIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As IGtolFrame
Dim IndicatorIndex As System.Integer
Dim value As System.Boolean
 
value = instance.DeleteIndicator(IndicatorIndex)
```

```

System.bool DeleteIndicator( 
   System.int IndicatorIndex
)
```

```

System.bool DeleteIndicator( 
   System.int IndicatorIndex
) 
```

#### Parameters

*IndicatorIndex*
:   One-based index of tolerance indicator to delete from the frame

#### Return Value

True if tolerance indicator successfully deleted, false if not

Remarks

Before calling this method, use [IGtolFrame:GetIndicatorCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicatorCount.md) to determine IndicatorIndex.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md)  
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.md)
