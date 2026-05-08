# ImportAnnotations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ImportAnnotations`

Imports the specified annotations into this drawing view.
Imports the specified annotations into this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ImportAnnotations( _
   ByVal IncludeDesignAnnotations As System.Boolean, _
   ByVal IncludeCosmeticThreads As System.Boolean, _
   ByVal IncludeDimXpertAnnotations As System.Boolean, _
   ByVal IncludeHiddenFeatureItems As System.Boolean, _
   ByVal Include3DViewAnnotations As System.Boolean _
) 
```

```

Dim instance As IView
Dim IncludeDesignAnnotations As System.Boolean
Dim IncludeCosmeticThreads As System.Boolean
Dim IncludeDimXpertAnnotations As System.Boolean
Dim IncludeHiddenFeatureItems As System.Boolean
Dim Include3DViewAnnotations As System.Boolean
 
instance.ImportAnnotations(IncludeDesignAnnotations, IncludeCosmeticThreads, IncludeDimXpertAnnotations, IncludeHiddenFeatureItems, Include3DViewAnnotations)
```

```

void ImportAnnotations( 
   System.bool IncludeDesignAnnotations,
   System.bool IncludeCosmeticThreads,
   System.bool IncludeDimXpertAnnotations,
   System.bool IncludeHiddenFeatureItems,
   System.bool Include3DViewAnnotations
)
```

```

void ImportAnnotations( 
   System.bool IncludeDesignAnnotations,
   System.bool IncludeCosmeticThreads,
   System.bool IncludeDimXpertAnnotations,
   System.bool IncludeHiddenFeatureItems,
   System.bool Include3DViewAnnotations
) 
```

#### Parameters

*IncludeDesignAnnotations*
:   True to import design annotations, false to not

*IncludeCosmeticThreads*
:   True to import cosmetic threads, false to not

*IncludeDimXpertAnnotations*
:   True to import DimXpert annotations, false to not

*IncludeHiddenFeatureItems*
:   True to import hidden feature items, false to not

*Include3DViewAnnotations*
:   True to import 3D view annotations, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
