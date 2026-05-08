# SetFrameSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols`

Obsolete. Superseded by IGtol::SetFrameSymbols2.
Obsolete. Superseded by [IGtol::SetFrameSymbols2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFrameSymbols( _
   ByVal FrameNumber As System.Short, _
   ByVal GCS As System.Short, _
   ByVal TolDia1 As System.Boolean, _
   ByVal TolMC1 As System.Short, _
   ByVal TolDia2 As System.Boolean, _
   ByVal TolMC2 As System.Short, _
   ByVal DatumMC1 As System.Short, _
   ByVal DatumMC2 As System.Short, _
   ByVal DatumMC3 As System.Short _
) 
```

```

Dim instance As IGtol
Dim FrameNumber As System.Short
Dim GCS As System.Short
Dim TolDia1 As System.Boolean
Dim TolMC1 As System.Short
Dim TolDia2 As System.Boolean
Dim TolMC2 As System.Short
Dim DatumMC1 As System.Short
Dim DatumMC2 As System.Short
Dim DatumMC3 As System.Short
 
instance.SetFrameSymbols(FrameNumber, GCS, TolDia1, TolMC1, TolDia2, TolMC2, DatumMC1, DatumMC2, DatumMC3)
```

```

void SetFrameSymbols( 
   System.short FrameNumber,
   System.short GCS,
   System.bool TolDia1,
   System.short TolMC1,
   System.bool TolDia2,
   System.short TolMC2,
   System.short DatumMC1,
   System.short DatumMC2,
   System.short DatumMC3
)
```

```

void SetFrameSymbols( 
   System.short FrameNumber,
   System.short GCS,
   System.bool TolDia1,
   System.short TolMC1,
   System.bool TolDia2,
   System.short TolMC2,
   System.short DatumMC1,
   System.short DatumMC2,
   System.short DatumMC3
) 
```

#### Parameters

*FrameNumber*

*GCS*

*TolDia1*

*TolMC1*

*TolDia2*

*TolMC2*

*DatumMC1*

*DatumMC2*

*DatumMC3*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
