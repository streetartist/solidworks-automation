# GetTransparency Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetTransparency`

Gets transparency parameters for this picture.
Gets transparency parameters for this picture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetTransparency( _
   ByRef Style As System.Integer, _
   ByRef Transparency As System.Double, _
   ByRef MatchingColor As System.Integer, _
   ByRef MatchingTolerance As System.Double _
) 
```

```

Dim instance As ISketchPicture
Dim Style As System.Integer
Dim Transparency As System.Double
Dim MatchingColor As System.Integer
Dim MatchingTolerance As System.Double
 
instance.GetTransparency(Style, Transparency, MatchingColor, MatchingTolerance)
```

```

void GetTransparency( 
   out System.int Style,
   out System.double Transparency,
   out System.int MatchingColor,
   out System.double MatchingTolerance
)
```

```

void GetTransparency( 
   [Out] System.int Style,
   [Out] System.double Transparency,
   [Out] System.int MatchingColor,
   [Out] System.double MatchingTolerance
) 
```

#### Parameters

*Style*
:   Style as defined by [swSketchPictureTransparencyStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchPictureTransparencyStyle_e.html)

*Transparency*
:   - 0 = opaque
    - 1 = transparent

    describing the relative transparency depending on the value of Style

*MatchingColor*
:   RGB color used as the transparent color when Style is swSketchPictureTransparencyUserDefined

*MatchingTolerance*
:   - 0 = exact match
    - 1 = less exact match

    indicating how closely MatchingColor must be to be considered a transparent color when Style is swSketchPictureTransparencyUserDefined

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)
