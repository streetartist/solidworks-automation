# GetLoopCount Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetLoopCount`

Gets the number of loops on which to create a single radius fillet.
Gets the number of loops on which to create a single radius fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLoopCount() As System.Integer
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer
 
value = instance.GetLoopCount()
```

```

System.int GetLoopCount()
```

```

System.int GetLoopCount(); 
```

#### Return Value

Number of loops

Remarks

Call this method before calling [ISimpleFilletFeatureData2::IGetLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetLoops.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetLoops.md)  
[ISimpleFilletFeatureData2::Loops Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Loops.md)
