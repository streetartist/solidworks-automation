# SetBalloonPadding Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloonPadding`

Sets the padding for this balloon note.
Sets the padding for this balloon note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBalloonPadding( _
   ByVal Padding As System.Double _
) As System.Boolean
```

```

Dim instance As INote
Dim Padding As System.Double
Dim value As System.Boolean
 
value = instance.SetBalloonPadding(Padding)
```

```

System.bool SetBalloonPadding( 
   System.double Padding
)
```

```

System.bool SetBalloonPadding( 
   System.double Padding
) 
```

#### Parameters

*Padding*
:   Balloon padding

#### Return Value

True if padding is successfully set, false if not

Remarks

This method is valid only if [INote::GetBalloonSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.md) is set to [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF\_Tightest.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetBalloonPadding Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonPadding.md)  
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.md)
