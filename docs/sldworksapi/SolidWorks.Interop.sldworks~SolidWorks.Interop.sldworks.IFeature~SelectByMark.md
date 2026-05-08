# SelectByMark Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SelectByMark`

Obsolete. Superseded by IFeature::Select2.
Obsolete. Superseded by [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByMark( _
   ByVal AppendFlag As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

```

Dim instance As IFeature
Dim AppendFlag As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean
 
value = instance.SelectByMark(AppendFlag, Mark)
```

```

System.bool SelectByMark( 
   System.bool AppendFlag,
   System.int Mark
)
```

```

System.bool SelectByMark( 
   System.bool AppendFlag,
   System.int Mark
) 
```

#### Parameters

*AppendFlag*

*Mark*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
