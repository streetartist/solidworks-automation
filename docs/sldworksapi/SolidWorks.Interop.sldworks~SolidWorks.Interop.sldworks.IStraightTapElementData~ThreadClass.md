# ThreadClass Property (IStraightTapElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~ThreadClass`

Gets or sets the thread class for this straight tap hole element.
Gets or sets the thread class for this straight tap hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThreadClass As System.Integer
```

```

Dim instance As IStraightTapElementData
Dim value As System.Integer
 
instance.ThreadClass = value
 
value = instance.ThreadClass
```

```

System.int ThreadClass {get; set;}
```

```

property System.int ThreadClass {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Thread class as defined in [swStraightTapHoleThreadClass\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightTapHoleThreadClass_e.html)

Remarks

This property is valid only if [IStraightTapElementData::ThreadClassOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~ThreadClassOverride.md) is set to true.

Example

See the [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md)  
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.md)
