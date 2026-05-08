# SetFrameSymbols2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2`

Sets the symbols for the specified frame.
Sets the symbols for the specified frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFrameSymbols2( _
   ByVal FrameNumber As System.Short, _
   ByVal GCS As System.String, _
   ByVal TolDia1 As System.Boolean, _
   ByVal TolMC1 As System.String, _
   ByVal TolDia2 As System.Boolean, _
   ByVal TolMC2 As System.String, _
   ByVal DatumMC1 As System.String, _
   ByVal DatumMC2 As System.String, _
   ByVal DatumMC3 As System.String _
) 
```

```

Dim instance As IGtol
Dim FrameNumber As System.Short
Dim GCS As System.String
Dim TolDia1 As System.Boolean
Dim TolMC1 As System.String
Dim TolDia2 As System.Boolean
Dim TolMC2 As System.String
Dim DatumMC1 As System.String
Dim DatumMC2 As System.String
Dim DatumMC3 As System.String
 
instance.SetFrameSymbols2(FrameNumber, GCS, TolDia1, TolMC1, TolDia2, TolMC2, DatumMC1, DatumMC2, DatumMC3)
```

```

void SetFrameSymbols2( 
   System.short FrameNumber,
   System.string GCS,
   System.bool TolDia1,
   System.string TolMC1,
   System.bool TolDia2,
   System.string TolMC2,
   System.string DatumMC1,
   System.string DatumMC2,
   System.string DatumMC3
)
```

```

void SetFrameSymbols2( 
   System.short FrameNumber,
   System.String^ GCS,
   System.bool TolDia1,
   System.String^ TolMC1,
   System.bool TolDia2,
   System.String^ TolMC2,
   System.String^ DatumMC1,
   System.String^ DatumMC2,
   System.String^ DatumMC3
) 
```

#### Parameters

*FrameNumber*
:   Feature control frame 1 for first

*GCS*
:   Geometric tolerance symbol (see **Remarks**)

*TolDia1*
:   Diameter symbol exists for tolerance 1 (True or false)

*TolMC1*
:   Material condition symbol for tolerance 1 (see **Remarks**)

*TolDia2*
:   Diameter symbol exists for tolerance 2 (True or false)

*TolMC2*
:   Material condition symbol for tolerance 2 (see **Remarks**)

*DatumMC1*
:   Material condition symbols for primary datum (see **Remarks**)

*DatumMC2*
:   Material condition symbols for secondary datum (see **Remarks**)

*DatumMC3*
:   Material condition symbols for tertiary datum (see **Remarks**)

Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

GTol symbols are defined in **C:\ProgramData\SolidWorks\SolidWorks** **20***nn***\lang\english\**gtol.sym. Reference this file to specify GCS, TolMC1, TolMC2, DatumMC1, DatumMC2, and DatumMC3 in <*LibraryName-SymbolName*> format.

Examples:

- GCS = "<IGTOL-POSI>" (Position symbol in the ISO Geometric Tolerancing Symbols library)
- TolMC1 = "<MOD-LMC>" (Least Material Condition symbol in the Modifying Symbols library)

After calling this method, call [IGtol::SetFrameValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues2.md) to specify tolerance and datum values.

Example

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)  
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)  
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

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
[IGtol::IGetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.md)  
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.md)  
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.md)
