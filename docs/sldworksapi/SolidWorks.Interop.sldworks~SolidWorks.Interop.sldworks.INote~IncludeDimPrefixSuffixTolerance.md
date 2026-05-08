# IncludeDimPrefixSuffixTolerance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IncludeDimPrefixSuffixTolerance`

Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note.
Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeDimPrefixSuffixTolerance As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.IncludeDimPrefixSuffixTolerance = value
 
value = instance.IncludeDimPrefixSuffixTolerance
```

```

System.bool IncludeDimPrefixSuffixTolerance {get; set;}
```

```

property System.bool IncludeDimPrefixSuffixTolerance {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to include the dimension prefix, suffix, and tolerance; false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
