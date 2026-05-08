# Select Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select`

Obsolete. Superseded by IFeature::Select2.
Obsolete. Superseded by [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IFeature
Dim AppendFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.Select(AppendFlag)
```

```

System.bool Select( 
   System.bool AppendFlag
)
```

```

System.bool Select( 
   System.bool AppendFlag
) 
```

#### Parameters

*AppendFlag*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
