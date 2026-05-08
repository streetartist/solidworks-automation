# SelectionState Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~SelectionState`

Gets or sets the side of the model to keep or remove.
Gets or sets the side of the model to keep or remove.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectionState As System.Integer
```

```

Dim instance As IIndentFeatureData
Dim value As System.Integer
 
instance.SelectionState = value
 
value = instance.SelectionState
```

```

System.int SelectionState {get; set;}
```

```

property System.int SelectionState {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Side of the model to keep or remove as defined in [swIndentSelectionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swIndentSelectionState_e.html)

Remarks

Setting this property inverts the side of the [target body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.md) to indent.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)  
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.md)
