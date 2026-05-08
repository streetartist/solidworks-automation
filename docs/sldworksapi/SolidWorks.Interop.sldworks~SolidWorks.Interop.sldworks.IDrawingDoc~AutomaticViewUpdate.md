# AutomaticViewUpdate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutomaticViewUpdate`

Gets or sets whether the drawing views in this drawing are automatically updated if the underlying model in that drawing view changes.
Gets or sets whether the drawing views in this drawing are automatically updated if the underlying model in that drawing view changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutomaticViewUpdate As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim value As System.Boolean
 
instance.AutomaticViewUpdate = value
 
value = instance.AutomaticViewUpdate
```

```

System.bool AutomaticViewUpdate {get; set;}
```

```

property System.bool AutomaticViewUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True updates the views automatically, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
