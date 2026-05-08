# PatternedTransforms Property (ICThread)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~PatternedTransforms`

Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.
Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PatternedTransforms As System.Object
```

```

Dim instance As ICThread
Dim value As System.Object
 
value = instance.PatternedTransforms
```

```

System.object PatternedTransforms {get;}
```

```

property System.Object^ PatternedTransforms {
   System.Object^ get();
}
```

#### Property Value

Array of [transforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) for the instances of this cosmetic thread

Remarks

The value returned by this property does not include this cosmetic thread, which is the seed feature and not an pattern instance.  Therefore, if this cosmetic thread is not used in a pattern feature, then [ICThreadFeatureData::GetTransformsPatternedCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetPatternedTransformsCount.md) returns 0 and this property returns an empty array.

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
