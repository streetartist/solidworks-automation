# CurrentParagraph Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph`

Gets or sets the current paragraph.
Gets or sets the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurrentParagraph As System.Integer
```

```

Dim instance As IParagraphs
Dim value As System.Integer
 
instance.CurrentParagraph = value
 
value = instance.CurrentParagraph
```

```

System.int CurrentParagraph {get; set;}
```

```

property System.int CurrentParagraph {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

0-based index of current paragraph

Remarks

Before calling any of the methods of [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md), you must call this method to set the current paragraph.

Use [IParagraphs::Count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~Count.md) to determine the index with which to set this property.

Example

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)
