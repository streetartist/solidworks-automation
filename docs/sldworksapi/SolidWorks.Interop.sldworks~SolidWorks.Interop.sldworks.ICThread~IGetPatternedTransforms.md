# IGetPatternedTransforms Method (ICThread)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetPatternedTransforms`

Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.
Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPatternedTransforms( _
   ByVal Count As System.Integer _
) As MathTransform
```

```

Dim instance As ICThread
Dim Count As System.Integer
Dim value As MathTransform
 
value = instance.IGetPatternedTransforms(Count)
```

```

MathTransform IGetPatternedTransforms( 
   System.int Count
)
```

```

MathTransform^ IGetPatternedTransforms( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Size of the output array (see **Remarks**)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of interface pointers to the [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) objects of the instances of this cosmetic thread

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ICThreadFeatureData::GetPatternedTransformsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetPatternedTransformsCount.md) before calling this method to determine the size of the output array.

The value returned by this method does not include this cosmetic thread, which is the seed feature and not an pattern instance. Therefore, if this cosmetic thread is not used in a pattern feature, then ICThreadFeatureData::GetPatternedTransformsCount returns 0 and this method returns an empty array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)  
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.md)  
[ICThread::PatternedTransforms Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~PatternedTransforms.md)
