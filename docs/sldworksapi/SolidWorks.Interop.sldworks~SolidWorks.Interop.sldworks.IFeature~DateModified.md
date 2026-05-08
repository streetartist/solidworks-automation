# DateModified Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateModified`

Gets the date on which the feature was last modified.
Gets the date on which the feature was last modified.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DateModified As System.String
```

```

Dim instance As IFeature
Dim value As System.String
 
value = instance.DateModified
```

```

System.string DateModified {get;}
```

```

property System.String^ DateModified {
   System.String^ get();
}
```

#### Property Value

Date on which the feature was last modified

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::CreatedBy Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CreatedBy.md)  
[IFeature::DateCreated Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateCreated.md)
