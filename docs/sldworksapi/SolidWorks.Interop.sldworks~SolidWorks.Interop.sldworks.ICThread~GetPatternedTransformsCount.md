# GetPatternedTransformsCount Method (ICThread)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetPatternedTransformsCount`

Gets the number of instances of this cosmetic thread that are patterns of this feature.
Gets the number of instances of this cosmetic thread that are patterns of this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPatternedTransformsCount() As System.Integer
```

```

Dim instance As ICThread
Dim value As System.Integer
 
value = instance.GetPatternedTransformsCount()
```

```

System.int GetPatternedTransformsCount()
```

```

System.int GetPatternedTransformsCount(); 
```

#### Return Value

Number of instances of this cosmetic thread that are patterns of this feature

Remarks

The value returned by this method does not include this cosmetic thread, which is the seed feature and not an instance of the pattern. Therefore, if this cosmetic thread is not used in any pattern feature, then this method returns 0.

Use this method before using [ICThread::IGetPatternedTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetPatternedTransforms.md) to determine the size of the array to pass to that method.

Example

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)  
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.md)  
[ICThread::PatternedTransforms Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~PatternedTransforms.md)
