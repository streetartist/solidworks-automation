# PatternId Property (IFaceHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~PatternId`

Gets the pattern ID of this face hatch. Read-only.
Gets the pattern ID of this face hatch. Read-only.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternId As System.Integer
```

```

Dim instance As IFaceHatch
Dim value As System.Integer
 
instance.PatternId = value
 
value = instance.PatternId
```

```

System.int PatternId {get; set;}
```

```

property System.int PatternId {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Pattern IDs as found in <install\_dir>\lang\<language>\SLDWRKS.PTN

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.md)
