# ViewOnly Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly`

Gets or sets whether to open the assembly document in Large Design Review mode.
Gets or sets whether to open the assembly document in Large Design Review mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ViewOnly As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.ViewOnly = value
 
value = instance.ViewOnly
```

```

System.bool ViewOnly {get; set;}
```

```

property System.bool ViewOnly {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to open the assembly in Large Design Review mode, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)  
[IConfiguration::LargeDesignReviewMark Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~LargeDesignReviewMark.md)
