# ThreadClass Property (ITaperedTapElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~ThreadClass`

Gets or sets the thread class for this tapered tap hole element.
Gets or sets the thread class for this tapered tap hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThreadClass As System.Integer
```

```

Dim instance As ITaperedTapElementData
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

Thread class as defined in [swTaperedTapThreadClass\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTaperedTapThreadClass_e.html)

Remarks

This property is valid only if [ITaperedTapElementData::ThreadClassOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~ThreadClassOverride.md) is set to true.

Example

See the [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaperedTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.md)  
[ITaperedTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData_members.md)
