# SetFrameValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues`

Obsolete. Superseded by IGtol::SetFrameValues2.
Obsolete. Superseded by [IGtol::SetFrameValues2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFrameValues( _
   ByVal FrameNumber As System.Short, _
   ByVal Tol1 As System.String, _
   ByVal Tol2 As System.String, _
   ByVal Datum1 As System.String, _
   ByVal Datum2 As System.String, _
   ByVal Datum3 As System.String _
) 
```

```

Dim instance As IGtol
Dim FrameNumber As System.Short
Dim Tol1 As System.String
Dim Tol2 As System.String
Dim Datum1 As System.String
Dim Datum2 As System.String
Dim Datum3 As System.String
 
instance.SetFrameValues(FrameNumber, Tol1, Tol2, Datum1, Datum2, Datum3)
```

```

void SetFrameValues( 
   System.short FrameNumber,
   System.string Tol1,
   System.string Tol2,
   System.string Datum1,
   System.string Datum2,
   System.string Datum3
)
```

```

void SetFrameValues( 
   System.short FrameNumber,
   System.String^ Tol1,
   System.String^ Tol2,
   System.String^ Datum1,
   System.String^ Datum2,
   System.String^ Datum3
) 
```

#### Parameters

*FrameNumber*
:   Feature control frame 1 for first

*Tol1*
:   Tolerance 1 value

*Tol2*
:   Tolerance 2 value

*Datum1*
:   Datum reference 1 (primary datum)

*Datum2*
:   Datum reference 2 (secondary datum)

*Datum3*
:   Datum reference 3 (tertiary datum)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetFrameCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.md)  
[IGtol::GetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.md)  
[IGtol::GetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.md)  
[IGtol::GetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.md)  
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.md)  
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.md)  
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.md)
