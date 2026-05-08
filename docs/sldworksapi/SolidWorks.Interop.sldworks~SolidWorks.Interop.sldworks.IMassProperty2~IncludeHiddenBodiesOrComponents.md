# IncludeHiddenBodiesOrComponents Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents`

Gets or sets whether to include the mass properties of hidden bodies/components.
Gets or sets whether to include the mass properties of hidden bodies/components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeHiddenBodiesOrComponents As System.Boolean
```

```

Dim instance As IMassProperty2
Dim value As System.Boolean
 
instance.IncludeHiddenBodiesOrComponents = value
 
value = instance.IncludeHiddenBodiesOrComponents
```

```

System.bool IncludeHiddenBodiesOrComponents {get; set;}
```

```

property System.bool IncludeHiddenBodiesOrComponents {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to include the mass properties of hidden bodies/components, false to not

Remarks

After setting this property to true, be sure to call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.md) before using the IMassProperty2 properties.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)  
[IMassProperty2::SelectedItems Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems.md)
