# ISafeArrayUtility Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility`

Access the ISafeArrayUtility interface, which can:
Access the ISafeArrayUtility interface, which can:

- get an unpacked array of native SOLIDWORKS Dispatch-based objects of the same data type and return a packed Variant SafeArray to use in methods that requires passing a packed Variant SafeArray.
- get a packed Variant SafeArray and return an unpacked array of native SOLIDWORKS Dispatch-based objects of the same data type.
- get a Variant SafeArray and return the number of SafeArray objects in the Variant SafeArray and their data type.
- get and put a value in a Variant SafeArray of the same data type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISafeArrayUtility 
```

```

Dim instance As ISafeArrayUtility
```

```

public interface ISafeArrayUtility 
```

```

public interface class ISafeArrayUtility 
```

Remarks

The ISafeArrayUtility interface replaces the SOLIDWORKS SafeArray template class, which you might have used in earlier versions of SOLIDWORKS to instantiate SafeArrays for methods requiring Variant arrays in your C++ projects.

This ISafeArrayUtility interface's methods are only compatible with raw pointers and BSTRs; this interface's methods are not compatible with smart pointers (i.e., reference counted) or the Active Template Library (ATL) class CComBSTR. For example:

:   :   IDispatch\* pDisp1;  //This works
    :   IDispatchPtr pDisp2 //This does not work
    :   CComPtr<IDispatch> pDisp3 //This does not work
    :   BSTR fileName1 //This works
    :   CComBSTR fileName2 //This does not work

Example

[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)  
[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)  
[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)  
[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
