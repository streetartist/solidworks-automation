# MoldDraftAnalysis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MoldDraftAnalysis`

Performs a mold draft analysis.
Performs a mold draft analysis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub MoldDraftAnalysis( _
   ByVal Angle As System.Double, _
   ByVal Options As System.Integer, _
   ByVal Colors As System.Object, _
   ByVal Shows As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Angle As System.Double
Dim Options As System.Integer
Dim Colors As System.Object
Dim Shows As System.Integer
 
instance.MoldDraftAnalysis(Angle, Options, Colors, Shows)
```

```

void MoldDraftAnalysis( 
   System.double Angle,
   System.int Options,
   System.object Colors,
   System.int Shows
)
```

```

void MoldDraftAnalysis( 
   System.double Angle,
   System.int Options,
   System.Object^ Colors,
   System.int Shows
) 
```

#### Parameters

*Angle*
:   Reference draft angle

*Options*
:   Analysis options as defined in [swDraftAnalysisOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisOptions_e.html)

*Colors*
:   Array of 4 colors (positive draft, negative draft, no draft, straddled faces)

*Shows*
:   Show each draft type as defined in [swDraftAnalysisShow\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisShow_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
