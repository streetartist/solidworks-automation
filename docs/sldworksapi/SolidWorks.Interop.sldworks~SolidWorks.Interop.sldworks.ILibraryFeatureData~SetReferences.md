# SetReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences`

Sets the references for the library feature.
Sets the references for the library feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetReferences( _
   ByVal RefVar As System.Object _
) 
```

```

Dim instance As ILibraryFeatureData
Dim RefVar As System.Object
 
instance.SetReferences(RefVar)
```

```

void SetReferences( 
   System.object RefVar
)
```

```

void SetReferences( 
   System.Object^ RefVar
) 
```

#### Parameters

*RefVar*
:   Array of references

Remarks

Some SolidWorks properties and methods, such as this method, have an input object that must be marshaled to an IDispatch object array because System.Object has replaced VARIANT in the .NET framework. When marshaling System.Object to an IDispatch object array, you must explicitly control the marshaling behavior by using the System.Runtime.InteropServices.DispatchWrapper class. See the VB.NET and C# examples in this Help topic and [IDispatch Object Arrays as Input in .NET](sldworksAPIProgGuide.chm::/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm) for more information.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Create Library Feature With References (C#)](Create_Library_Feature_With_References_Example_CSharp.htm)  
[Create Library Feature With References (VB.NET)](Create_Library_Feature_With_References_Example_VBNET.htm)  
[Create Library Feature With References (VBA)](Create_Library_Feature_With_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::GetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences.md)  
[ILibraryFeatureData::GetReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.md)  
[ILibraryFeatureData::IGetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences.md)  
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.md)
